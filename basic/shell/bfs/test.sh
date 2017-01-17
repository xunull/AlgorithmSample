# aaa=(1 2 3)
#
# test() {
#   local test=$1
#   echo $1
#   echo ${test[@]}
#   echo $#
# }
#
#
# test ${aaa[@]}

function f() {
    name=$1[@]
    b=$2
    a=("${!name}")

    for i in "${a[@]}" ; do
        echo "$i"
    done
    echo "b: $b"
}

x=("one two" "LAST")
b='even more'

f x "$b"
