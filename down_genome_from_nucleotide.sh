#!/usr/bin/sh
while getopts ":f:i:" optname
do
    case "$optname" in
      "i")
        pubmedid=$OPTARG
        ;;
        ":")
        echo "No argument value for option $OPTARG"
        ;;
        "?")
        echo "Unknown option $OPTARG"
        ;;
        *)
        echo "Unknown error while processing options"
        ;;
    esac
done

mkdir ./$pubmedid
if [ $pubmedid ]; then
    wget -qO ./$pubmedid/$pubmedid.gff "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=gff3&id=$pubmedid"
    wget -qO ./$pubmedid/$pubmedid.fa "https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?db=nuccore&report=fasta&id=$pubmedid"

    echo -e "\n==================\n"
    echo -e "The genome has download in $pubmedid files !\n"
    echo -e "=================="
else
    echo -e "\n==================\n"
    echo -e "please check the '-i name' again\n"
    echo -e "=================="
fi