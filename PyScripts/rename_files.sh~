#renames filenames produced with MP3Fiber by removing substring
#usage: ./rename_files.sh <folder_to_clean>

parent_folder="/home/isaykatsman/Desktop/client_destination"

for name in $parent_folder/*MP3Fiber*
do
    newname="$(echo "$name" | sed -i 's/\[www\.MP3Fiber\.com\]//g')"
    mv "$name" "$newname"
    echo $newname
done
