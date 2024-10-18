import numpy as np
import matplotlib.pyplot as plt


code_index = 1
chroms = [f'chr{i}' for i in list(range(1, 23)) + ['X']]


def APA(loop_samples,name):
    colors = ['blue', 'red', 'orange']
    plt.figure(figsize=(6, 4))
    for i, sample in enumerate(loop_samples):
        lengths = []
        print(' ', sample)
        f = open(loop_samples[sample])
        for line in f:
            lst = line.strip().split()
            if lst[0] not in chroms:
                continue
            p11, p12, p21, p22 = int(lst[1]), int(lst[2]), int(lst[4]), int(lst[5])
            if (p12 - p11) < (p22 - p21):
                length = p22 - p21
            else:
                length = p12 - p11
            lengths.append(np.log10(length))

        plt.hist(lengths, bins=50, range=(4.8, 6.5), color=colors[i], alpha=0.4, label=sample)

    plt.legend()
 #   plt.ylim([0, 200])
    plt.tight_layout()
    plt.savefig(f"{name}_length_dist.png")
    plt.show()


def APA2(loop_samples,name):
    # colors = ['blue', 'red', 'orange']
    colors = ['blue', 'orange']
    plt.figure(figsize=(6, 4))
    for i, sample in enumerate(loop_samples):
        lengths = []
        print(' ', sample)
        f = open(loop_samples[sample])
        for line in f:
            lst = line.strip().split()
            if lst[0] not in chroms:
                continue
            p11, p12, p21, p22 = int(lst[1]), int(lst[2]), int(lst[4]), int(lst[5])
            if (p12 - p11) < (p22 - p21):
                length = p12 - p11
            else:
                length = p22 - p21
            lengths.append(length / 10000)

        plt.hist(lengths, bins=10, range=(0, 10), color=colors[i], alpha=0.4, label=sample)

    plt.legend()
#    plt.ylim([0, 200])
    plt.tight_layout()
    plt.savefig(f'{name}_width_dist.png')
    plt.show()


if __name__ == '__main__':
    hic_path = '/nfs/turbo/umms-drjieliu/proj/4dn/data/bulkHiC/GM12878/GM12878.hic'
    name = "063124_All_EP"
    samples1 = {
        'Quagga': '/home/spmoran/temp_smoran/Fan_StripeCaller/2024_SummerPublishPush/ctcf_deficient/Othermodels/Quagga_GM12878_EP.txt',
    #    'Zebra': '/home/spmoran/temp_smoran/Fan_StripeCaller/2024_SummerPublishPush/ctcf_deficient/Othermodels/Zebra_AB_Merged_GM12878_EP.txt',
        'StripeNN': '/home/spmoran/temp_smoran/Fan_StripeCaller/2024_SummerPublishPush/ctcf_deficient/Othermodels/StripeNN_GM12878_EP.txt',
    }
    samples2 = {
        'Quagga': '/home/spmoran/temp_smoran/Fan_StripeCaller/2024_SummerPublishPush/ctcf_deficient/Othermodels/Quagga_GM12878_EP.txt',
        'Zebra': '/home/spmoran/temp_smoran/Fan_StripeCaller/2024_SummerPublishPush/ctcf_deficient/Othermodels/Zebra_AB_Merged_GM12878_EP.txt',
        'StripeNN': '/home/spmoran/temp_smoran/Fan_StripeCaller/2024_SummerPublishPush/ctcf_deficient/Othermodels/StripeNN_GM12878_EP.txt',
    }

    APA(
        loop_samples=samples2,name=name
    )

    APA2(
        loop_samples=samples1,name=name
    )

