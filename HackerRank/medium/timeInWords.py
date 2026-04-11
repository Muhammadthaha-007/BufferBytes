def timeInWords(h, m):
    if h < 13 and h > 0:
        hours = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
        hours_num = [x for x in range(1,13)]

        minutes = [
            "o' clock","one","two","three","four","five","six","seven","eight","nine","ten",
            "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen","twenty",
            "twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty",
            "thirty one","thirty two","thirty three","thirty four","thirty five","thirty six","thirty seven","thirty eight","thirty nine","fourty",
            "fourty one","fourty two","fourty three","fourty four","fourty five","fourty six","fourty seven","fourty eight","fourty nine","fifty",
            "fifty one","fifty two","fifty three","fifty four","fifty five","fifty six","fifty seven","fifty eight","fifty nine"
            ]
        minutes_num = [x for x in range(1,60)]

        special_words = ["minute","minutes","past","to","half","quarter",]
        hrs = ""
        mns = ""

        for hr in hours_num:
            if h == hr:
                hrs += hours[hr]

        for mn in minutes_num:
            if m == 0:
                mns += minutes[0]
                break
            elif m == 1:
                mns += minutes[1] +" "+ special_words[0] +" "+ special_words[2]
                break
            elif m == 15:
                mns += special_words[5] +" "+ special_words[2]
                break
            elif m == mn:
                if m < 30 and m != 15:
                    mns += minutes[mn] +" "+ special_words[1] +" "+ special_words[2]
                elif m == 30:
                    mns += special_words[-2] +" "+ special_words[2]
                elif m == 45:
                    mns += special_words[5] +" "+ special_words[3]
                elif m > 30 and m != 45 and m < 60:
                    mns += minutes[60 - mn] +" "+special_words[1] +" "+ special_words[3]
        if m == 00:     
            return hrs +" "+ mns
        elif m <= 30:
            return mns +" "+ hrs
        elif m > 30 and m < 60:
            return mns +" "+ hours[h+1]

print(timeInWords(8,29))