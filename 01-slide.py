#project_9522_spaced_data.py

def process_file(reader):
    """ (file open for reading) -> new file format
    Read and process reader, which must start with a time_series_header.
    if list passed from text_to_list is empty(blank line)
    do nothing, if the list passed from text_to_list begins with spec,
    write the contents of measeure list to the new file, clear measure &
    set the value of the first item to Spec item.  If the list contains data,
    append to measure.
    """
    
    result_line= ''
    result=''
    prod=''
    count=0    #count for === line for prod
    first_var='-------'
    first_count =0    #count for first prod for --- line for prod
    
    #
    #result_line = product_line(line)
    #measure.append(result_line)

    #first we need to add headers
    with open('9522_new.csv', 'a') as output_file:
        output_file.write('"DEPT","PRODUCT","IPNUM","RPTSEQ","FDRSYS","FDRKEY"' +'\n')
        
    #subs times
    for line in reader:
        line=line.strip()    #removes leading/trailing whitespace
        field = line.split()
        if len(field)>0 and len(field)<2:
            for e in range(len(field)):
                #to find product description find === line before
                if field[e].startswith('==='):
                    count = 1
                    prod=''
                
        elif len(field)>3:
            ##print('001-field=',field)
            for i in range(0,2):
                #find dept         
                if field[i] == 'DEPT:':
                    #save DEPT
                    dept=field[i+1]
                    ##deptname? from field(i+3 to end)
                #to find first product description find --- line before
                
                if field[i] == first_var:
                    first_count = 1
                    prod=''
                    break          
                #
                #find first prod desc
                if first_count == 1:
                    #after first item update first_var
                    first_var='datasci'
                    for f in range(len(field)):
                        if field[f]=='FDE':
                            #don't want any info after FDE
                            first_count=10
                            break
                        else:
                            prod=prod+field[f]+' '
                            #redundant
                            count=0
                            first_count=10
                        
                #find prod desc
                #'hardcode' in the startswith field[0] instead of using i
                if (count >0 and not field[0].startswith('*') and not field[0].startswith('DCM')
                        and not field[0].startswith('RUN')and not field[0].startswith('BILL') and not
                        field[0].startswith('FISCAL') and not field[0].startswith('DEPT:') and not
                        field[0].startswith('PRODUCT')and not field[0].startswith('-------')):
                    ##print ('count at not *=',count)
                    ##print('field[i]=',field[i])
                    ##print('field=',field)
                    for d in range(len(field)):
                        if field[d]=='FDE':
                            #don't want any info after FDE
                            count=0
                            break
                        else:
                            prod=prod+field[d].replace(","," ")+' '
                            #https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch02s11.html
                            # If you needed to do something to the inner space, you would need to use another technique, such as using the replace() method or a regular expression substitution.
                            #redundant
                            count=0
                            
                        
                #find IPNUM
                if field[i] == 'IP' and field[i+1] =='NUM':
                    #save IPNUM
                    ipnum=field[i+2].strip(':')
                #find RPT Seq
                if field[i] == 'RPT' and field[i+1].startswith('SEQ:'):
                    #save RPT SEQ
                    rptseq =field[i+1].strip('SEQ:')
                #find FDR SYS
                if field[i] == 'FDR' and field[i+1].startswith('SYS:'):
                    #(Kudgel) strip SYS deletes the leading/trailing S from the fdrsys
                    if field[i+1] == 'SYS:SUR':
                        #save FDR SYS
                        fdrsys='SUR'
                    else:
                        #save FDR SYS
                        fdrsys=field[i+1].lstrip('SYS:')  #lstrip accounts for ECS fdr system
                #find FDR KEY (last item before write to file)
                if field[i] == 'FDR' and field[i+1].startswith('KEY:'):
                        #(Kudgel)save FDR KEY
                        if field[i+2] == 'COST':   #for 'MEDIUM COST' fdrkey
                            fdrkey=field[i+1].lstrip('KEY:') + ' COST'
                        elif field[i+2] == 'DRUG':
                            fdrkey=field[i+1].lstrip('KEY:') + ' DRUG '+ field[i+3]
                        else:
                            fdrkey=field[i+1].lstrip('KEY:') #lstrip accounts for 'E'in fdrkey
                            
                        #when result has no data it is a blank line
                        ##print('20-result-line=', result_line)
                        if result_line != None:
                            with open('9522_new.csv', 'a') as output_file:
                                list_2_line=dept+','+prod+','+ipnum+','+rptseq+','+fdrsys+','+fdrkey
                                #print('list 2 line=',list_2_line)
                                output_file.write(list_2_line+'\n')
                                result=''
                                list_2_line=''
                
           

if __name__ == '__main__':
    with open('9522.txt', 'r') as input_file:
        process_file(input_file)


