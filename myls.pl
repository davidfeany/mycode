foreach(`ls -l`)
{
	chomp $_;
        @a = split(" +", $_);
	#print $a[0..4, $#a]
        printf("%s,%s,%s,%s,%s\n", @a[0,2,3,4,$#a]);
}
