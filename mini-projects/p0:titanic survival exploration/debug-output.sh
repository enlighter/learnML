i = 0
while read p; do
  if [ $((p - i)) == 0 ]
  then
    echo $p
  else
    echo "ok"
  fi

  ((i++))
done <output
