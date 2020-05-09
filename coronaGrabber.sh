for nation in "uk" "us" "italy" "spain" "germany"
    do
        URL="https://www.worldometers.info/coronavirus/country/"${nation}
        wget -O ${nation}.txt -nv "$URL"
    done
for nation in "uk" "us" "italy" "spain" "germany"
#for nation in "uk" 
    do
        if test -s ${nation}.txt
        then
            python coronaParser.py ${nation}.txt
        fi
    done
