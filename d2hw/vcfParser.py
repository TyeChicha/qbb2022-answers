#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []                      #initializing lists and dictionaries to be
    info_description = {}          
    info_type = {}
    format_description = {}
    type_map = {                    #conversion dictionary
        "Float": float,
        "Integer": int,
        "String": str
        }
    malformed = 0             #number of malformed lines initialized to 0

    try:
        fs = open(fname)            #open the file and if the file not thre indicate through error message
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

    for h, line in enumerate(fs):           #read through lines
        if line.startswith("#"):   #if a  header
            try:
                if line.startswith("##FORMAT"):                        #if a formst line
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","    #strip line and separate format from format infor
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):                                    #whle i less than number of fields
                        if fields[i] == "," and not in_string:                    #no clue
                            name, value = fields[start:i].split('=')         #no clue
                            if name == "ID":                                #
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else:
            try:
                fields = line.rstrip().split("\t")       #separate each column and enter into a list
                fields[1] = int(fields[1])                #make column 2 and int
                if fields[5] != ".":                    #if column 5 is not . 
                    fields[5] = float(fields[5])          #make it a float
                info = {}                              #initialize dictionary to hold info column8
                for entry in fields[7].split(";"):       #for each string in column 8 seperated by ;
                    temp = entry.split("=")              #separate info type and value in temmp variable
                    if len(temp) == 1:                   #if no value for info, set to 0
                        info[temp[0]] = None
                    else:                                 #else store the name and value
                        name, value = temp                 #use name and value to check var type and set correct type in dic entry
                        Type = info_type[name]
                        info[name] = type_map[Type](value)
                fields[7] = info                        #insert dictionary into column 8 of new file
                if len(fields) > 8:                      #if>8 columns split col 9 by : make list of values in column
                    fields[8] = fields[8].split(":")
                    if len(fields[8]) > 1:
                        for i in range(9, len(fields)):
                            fields[i] = fields[i].split(':')
                    else:                                   #otherwise just put into first slot
                        fields[8] = fields[8][0]
                vcf.append(fields)           # assemble new vcf
            except:
                malformed += 1    #bad line counter
    vcf[0][7] = info_description #fill in header info data
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description  #fill in header format data
    if malformed > 0:   #if there were bad lines send info to stderr
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    return vcf

if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
