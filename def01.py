def def01():
    src_alphabet="abcdefghijklmnopqrstuvwxyz".encode("utf-8")
    dst_alphabet="cdefghijklmnopqrstuvwxyzab".encode("utf-8")

    translation_table=bytearray.maketrans(src_alphabet, dst_alphabet)

    message="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    result=message.translate(translation_table)
    print(result)

    message="map"
    result=message.translate(translation_table)
    print(result)

if __name__ == "__main__":
    def01()
