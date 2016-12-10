# add header to chromosome gene data
echo "Starting combining files"

#alter so that it will take a folder as an argument using $1, similar to sys.argv

for file in “$@”
do
	cat header.txt $file > processed/$file
	echo "$file"
done

echo "Switching into new directory"
cd processed

for input in *.txt
do 
	echo "Analyzing $input ..."
	python gc_gene_plot_1.py $input
done
echo "Done!"

