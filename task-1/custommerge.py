import os
def merge(file_list,output_file):
    f_out = file(output_file,'w')
    sum = 0
    for f in file_list:
        f_in = file(f)
        num = int(f_in.read())
        sum += num
        f_in.close()
    save-path = "~/Downloads/"
    fname = "hello"
    fullname = os.path.join(save-path + fname)
    f1 = open(fullname, "w")
    f1.write(sum)
    f1.close()
    f_out.close()