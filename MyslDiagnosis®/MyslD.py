while True:
    pLPMS = ''
    
    while True:
        LPMS = input("State your feelings in no less than 50 words: " + str(pLPMS))
        LPMS = LPMS.lower()
        LPMS = LPMS.split()
        brk_con = 'y'
        
        if len(LPMS) < 50:
            while True:
                brk_con = input("The length is less than 50 words, which might lead to inaccurate answers. Do you still want to continue? [Y/N] ")
                brk_con = brk_con.lower()
                if brk_con in 'yn':
                    break
                else:
                    print("<!> Invalid answer.")
        
        if brk_con == 'y':
            break
        else:
            pLPMS = LPMS

    Anxiety_disorder = ['feel', 'people', "can't", 'cannot', 'wrong', 'not', 'feel good', 'ok', 'okay']
    ADscore = 0

    Depression = ["i'm", 'am', 'must', 'should', 'always', 'tired', 'hate', 'hurt', 'worse', 'angry', 'frustrated']
    Dscore = 0

    BPD = [['hate', 'love'], ['angry', 'happy'], ['perfect', 'weird'], ['fine', 'weird'], ["don't", 'do'], ['sorry', 'glad'], ['ok', 'not ok'], ['ok', 'not okay'], ['okay', 'not okay']]
    BPDscore = 0

    for word in LPMS:
        if word in Anxiety_disorder:
            ADscore += 1
        if word in Depression:
            Dscore += 1
        BPDindex = 0
        BPDloc = False
        BPDindexused = []
        BPDwordloc = ''
        
        for wpair in BPD:
            if word in wpair:
                if BPDindex in BPDindexused and word != BPDwordloc and BPDloc == True:
                    BPDscore += 2
                    BPDloc = False
                    BPDwordloc = ''
                else:
                    BPDloc = True
                    BPDindexused.append(BPDindex)
                    BPDwordloc = word
            BPDindex += 1
            
    sumscore = ADscore + BPDscore + Dscore
    
    if sumscore != 0:
        print("You are diagnosed to be: " + str((ADscore / sumscore) * 100) + "% Anxious. " + str((Dscore / sumscore) * 100) + "% Depressed. " + str((BPDscore / sumscore) * 100) + "% Bipolar.")
    elif sumscore == 0:
        print("JUST HOW!?!?!??!?")
    
    while True:
        con_con = input("Do you want to take the diagnosis again? [Y/N] ")
        con_con = con_con.lower()
        if con_con in 'yn':
            break
        else:
            print("<!> Invalid answer.")
    
    if con_con == 'n':
        break
