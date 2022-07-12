import re


def parse_mtype_descr(desc):
    """
    Parse Machine Type description and return vCPU number and RAM in GB
    :param desc: Raw description value from GCP API
    :return: {vcpu_num, ram_gb}
    """
    shared_core_flag = ' shared physical core)'
    # CPU number detection
    re_cpu = re.search("\\w+ vCPU", desc)
    vcpu_num = str(re_cpu[0]).split(" ")[0]
    if shared_core_flag in desc:
        # Work around for shared CPU cores
        re_sh_cpu = re.search(f"(\\w*\\W*\\w*{shared_core_flag}", desc)
        vcpu_sh_num = str(re_sh_cpu[0]).split(" ")[0]
        # print(f'vcpu_sh_num={vcpu_sh_num}')
        if vcpu_sh_num:
            if "/" in vcpu_sh_num:
                tmp_val = vcpu_sh_num.split("/")
                vcpu_num = int(vcpu_num) * int(tmp_val[0]) / int(tmp_val[1])
            else:
                vcpu_num = int(vcpu_num) * int(vcpu_sh_num)
    # RAM detection
    re_ram = re.search("[\\w.]+ \\w+ RAM", desc)
    ram_gb = str(re_ram[0]).split(" ")[0]
    ram_unit = str(re_ram[0]).split(" ")[1]
    # print(f'ram:{ram_gb}  unit:{ram_unit}')
    if ram_unit == 'TB':
        ram_gb = float(ram_gb) * 1024
    return vcpu_num, ram_gb


descs = list()

descs.append("Compute Optimized: 4 vCPUs, 16 GB RAM")
descs.append("Compute Optimized: 96 vCPUs, 1.4 TB RAM")
descs.append("1 vCPU, 3.75 GB RAM")
descs.append("1 vCPU (shared physical core) and 0.6 GB RAM")
descs.append("1 vCPU (shared physical core) and 1.7 GB RAM")
descs.append("Efficient Instance, 2 vCPU (1/2 shared physical core) and 4 GB RAM")
descs.append("Efficient Instance, 2 vCPU (1/4 shared physical core) and 2 GB RAM")
descs.append("Efficient Instance, 2 vCPU (1/8 shared physical core) and 1 GB RAM")

for val in descs:
    # print(f'{key} - {val}')
    cpun, ramn = parse_mtype_descr(val)
    print(f'CPU: {float(cpun):<6.2f} RAM: {float(ramn):<7.2f}   - FROM: {val}')
