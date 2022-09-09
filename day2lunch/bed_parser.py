#!/usr/bin/env python3

import sys

def parse_bed(fname):
    malformed=0
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, int, int, int, int]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        assert fieldN!=10 and fieldN!=11, "Error: BED10 and BED11 file types unsupported"
        if fieldN <3:
            print(f"Line {i} appears malformed", file=sys.stderr)
            malformed+=1
            continue
        try:
            for j in range(min(len(field_types), len(fields))):
                if(j==8):                                                      #if 9th column split by commas and insert into hold
                    hold=fields[j].split(",")
                    #hold=field_types[j](fields[j]).split(",")
                    for k in range(3):                                         #put 3 values into list fields[8][1-3]
                        #fields[j][k]=int(hold[k])
                        hold[k] = int(hold[k])
                    fields[j] = hold
                elif j==10:           #if block match block add list of block joints into column 11
                    hold=fields[j].split(",")
                    try:
                        len(hold)==fields[9]
                    except:
                        print('blocks (11) dont match block count in line ',i)
                        continue
                    for k in range(fields[9]):
                        hold[k] = int(hold[k])
                        fields[j]=hold
                    
                elif j==11:             #if block match block add list of block joints into column 12
                  hold=fields[j].split(",")
                  try:
                      len(hold)==fields[9]
                  except:
                      print('blocks (11) dont match block count in line ',i)
                      continue
                  for k in range(fields[9]):
                      hold[k] = int(hold[k])
                      fields[j]=hold
                else:
                    fields[j] = field_types[j](fields[j])                     #else just put the correct type in their
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    print('number of malformed lined: ' + str(malformed))
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    for line in bed:
        print (line)
