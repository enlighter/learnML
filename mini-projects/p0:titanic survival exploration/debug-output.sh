i = 1
while read p; do
  echo $p,$i
  if [ $((p - i)) == 0 ]
  then
    echo $p
  else
    echo "ok"
  fi

  ((i++))
done <output
