"""
Process epigenomic features into arrays
"""

import pyBigWig
import numpy as np
import os


# def download(
#         file='data_sources.txt',
#         output_path='/scratch/drjieliu_root/drjieliu/fanfeng/RCMC_Epi',
#         log_file='Epi_log.txt'
# ):
#     downloaded = []
#     if not os.path.exists(output_path):
#         os.mkdir(output_path)
#     f = open(log_file, 'w')
#     f.write('Downloading...\n')
#     for line in open(file):
#         if line.startswith('#') or len(line.strip()) == 0:
#             continue
#         lst = line.strip().split()
#         cell_type, assay, _, url = lst
# 
#         ########
#         if cell_type == 'H1':
#             continue
#         ########
# 
#         if not os.path.exists(f'{output_path}/{cell_type}'):
#             os.mkdir(f'{output_path}/{cell_type}')
#         try:
#             os.system(
#                 f'wget {url} -O {output_path}/{cell_type}/{cell_type}_{assay}_hg38.bigWig'
#             )
#             f.write(f' {cell_type} {assay} Success!\n')
#             downloaded.append((cell_type, assay))
#         except Exception as e:
#             f.write(f' {cell_type} {assay} Fail!\n')
#             f.write(str(e))
#     f.close()
#     return downloaded


def load_chrom_sizes(reference_genome):
    """
    Load chromosome sizes for a reference genome
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
#    rg_path = f'{my_path}/{reference_genome}.chrom.sizes'
    rg_path = "/home/spmoran/temp_smoran/Fan_StripeCaller/2024_Quagga/StripeCaller/Quagga/utils/reference_genome/hg38"
    f = open(rg_path)
    lengths = {}
    for line in f:
        [ch, l] = line.strip().split()
        lengths[ch] = int(l)
    return lengths


def load_bigWig_for_entire_genome(path, name, rg, resolution=200, epi_path=''):
    """
        Load bigwig file and save the signal as a 1-D numpy array

        Args:
            path (str): recommended: {cell_type}_{assay_type}_{reference_genome}.bigwig (e.g., mESC_CTCF_mm10.bigwig)
            name (str): the name for the epigenetic mark
            rg (str): reference genome
            resolution (int): resolution
            epi_path (str): the folders for storing data of all chromosomes

        No return value
        """
    bw = pyBigWig.open(path)
    chromosome_sizes = load_chrom_sizes(rg)
    del chromosome_sizes['chrY']
    chroms = chromosome_sizes.keys()

    if not os.path.exists(epi_path):
        os.mkdir(epi_path)

    for ch in chroms:
        if not os.path.exists(f'{epi_path}/{ch}'):
            os.mkdir(f'{epi_path}/{ch}')

        end_pos = chromosome_sizes[ch]
        nBins = end_pos // resolution
        end_pos = nBins * resolution  # remove the 'tail'

        vec = bw.stats(ch, 0, end_pos, exact=True, nBins=nBins)
        for i in range(len(vec)):
            if vec[i] is None:
                vec[i] = 0
        np.save(f'{epi_path}/{ch}/{ch}_{resolution}bp_{name}.npy', vec)


if __name__ == '__main__':
#    downloaded = download(
#        file='data_sources.txt',
#        output_path='/scratch/drjieliu_root/drjieliu/fanfeng/RCMC_Epi',
#        log_file='Epi_log.txt'
#    )
    # downloaded = [('GM12878', 'CTCF'),('GM12878', 'H3K4me2'), ('GM12878', 'H3K4me3'),('GM12878', 'H3K27ac')]
    # downloaded = [('H1', 'CTCF'),('H1', 'H3K4me2'), ('H1', 'H3K4me3'),('H1', 'H3K27ac')]
    downloaded = [('GIST-T1', 'CTCF'),('GIST-T1', 'H3K27ac'),]
    f = open('Epi_log.txt', 'a')
    f.write('Processing...\n')


    for (cell_type, assay) in downloaded:
        bw_path = '/nfs/turbo/umms-drjieliu/proj/Quagga/data' #take bigwig files from appropriate ENCODE/4DN source
        # in_path = f'{bw_path}/{cell_type}/ChIP-seq/{cell_type}_{assay}_hg38.bigWig'
        in_path = f'{bw_path}/{cell_type}/ChIP-seq/{cell_type}_{assay}_hg38.bw'
        out_path = f'/nfs/turbo/umms-drjieliu/usr/temp_smoran/Fan_StripeCaller/070324_GIST-T1_RCMC/DATA/OUTPATH/Epi/{cell_type}'
        try:
            load_bigWig_for_entire_genome(in_path, assay, 'hg38', 500, out_path)
            f.write(f' {cell_type} {assay} Success!\n')
        except Exception as e:
            f.write(f' {cell_type} {assay} Fail!\n')
            f.write(str(e))
    f.close()  
