SUFFIX_FROM=$1
OUT_FOLDER=$2
SUFFIX_TO=$3

set -e

if [ $# -ne 3 ]; then
        echo "Syntax: " $0 "<extension-in> <out-folder> <out-suffix>"
        exit 0
fi

SUFFIX_FROM_DOT="${SUFFIX_FROM}."

echo "Converting <image>.$SUFFIX_FROM images to <image>-$SUFFIX_TO.png"
echo

for name in *.$SUFFIX_FROM; do
	newname="${name%.*}$SUFFIX_TO.png"
        echo "Converting $name to $OUT_FOLDER/$newname"
	convert "$name" masks/mask.png -sample 240x240 -alpha Off -compose CopyOpacity -composite -density 180 -background transparent "$OUT_FOLDER/$newname"
	#convert "$OUT_FOLDER/$newname" -gravity center -extent 360x360 -density 180 -strip -background transparent "$OUT_FOLDER/$newname"

done

