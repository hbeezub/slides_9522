#9522_slide_IPNUM_only.py
def process_file(reader):
    ''' (file open for reading) -> new file format
    
    '''
    
    result_line= ''
    result=''
    slide="IPNUM" +'\n'

    #first we need to add headers
    with open('9522_slide_new.csv', 'a') as output_file:
        output_file.write('"IPNUM"' +'\n')

    #subs times
    for line in reader:
        line=line.strip()    #removes leading/trailing whitespace
        field = line.split()

        if len(field)>3:
            ##print('001-field=',field)
            for i in range(0,2):
                #find dept         
                          
                #find IPNUM
                if field[i] == 'IP' and field[i+1] =='NUM':
                    #save IPNUM
                    ipnum=field[i+2].strip(':')
                    


                        #(last item before write to file)
                        #when result has no data it is a blank line
                        ##print('20-result-line=', result_line)
                    if result_line != None:
                        with open('9522_slide_new.csv', 'a') as output_file:
                            list_2_line=ipnum
                            slide=slide+list_2_line+'\n'
                            #print('list 2 line=',list_2_line)
                            output_file.write(list_2_line+'\n')
                            result=''
                            list_2_line=''
                
    print(slide)       
    
if __name__ == '__main__':
    with open('9522_slide.txt', 'r') as input_file:
        process_file(input_file)

