var  PROGRAMMERS_SECRET = "_:D_";
var  BAD_CHAR = "`";

fun safeString(s: String): String {
   return s.replace(BAD_CHAR, PROGRAMMERS_SECRET)    
}

fun main() {
    println(safeString("`ls -l`"));
    println("`echo me`")
}