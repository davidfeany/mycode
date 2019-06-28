foreach(`ls -l`)
{
        @a = split(" +", $_);
	#print $a[0..4, $#a]
        printf("%s", $a[0]);
        printf("%s", $a[4]);
}
