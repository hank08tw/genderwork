#!bin/sh
#cat ../List/gender/train.txt
FILE=../List/gender/test.txt

# This is correct way to read file.
echo "################################"
k=1
female_num=0
male_num=0
while read line;do
        line_arr=($line)
        #調用並變成array
        #pic_name=${line_arr[0]}

        pic_label=${line_arr[1]}
        #調用array第二個元素
        #echo $pic_name $pic_label
        #echo "Line # $k: $pic_name###$pic_label"
        #1是男性，0是女性
        if ((pic_label == "0"))
        then
            first="../Dataset/gender/${line_arr[0]}"
            second="./data/test/female.$female_num.jpg"
            echo $first
            echo $second
            cp $first $second
            ((female_num++))
        else
            first="../Dataset/gender/${line_arr[0]}"
            second="./data/test/male.$male_num.jpg"
            echo $first
            echo $second
            cp $first $second
            ((male_num++))
        fi 
        ((k++))
done < $FILE
echo "Total number of lines in file: $k"

