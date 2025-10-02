  889  sed 's/solero/solaris/' file-list.txt
  890  sed 's/solero/solaris/' file-list.txt > file-list-solaris.txt
  894  cat /etc/hosts > hosts.txt
  895  cat hosts.txt
  896  sed -n '5 p' hosts.txt
  897  sed '5 p' hosts.txt
  898  sed -n '1~3 =' hosts.txt
  899  sed -n '$ =' hosts.txt
  900  clear
  901  sed -n '$ =' hosts.txt
  902  sed -n '$ p' hosts.txt
  903  sed -n '/[[:xdigit:]]/ p' hosts.txt
  904  sed -n '/[0-9a-f]{4}/ p' hosts.txt
  905  sed -n '/f*/ p' hosts.txt
  906  clear
  907  sed -n '/ip6/ p' hosts.txt
  908  sed -n '/[0-9a-f]{4}/ p' hosts.txt
  909  sed -n '/[0-9a-f]*/ p' hosts.txt
  910  sed -n '/[[:digit::]]/ p' hosts.txt
  911  sed -n '/[0-9]/ p' hosts.txt
  912  sed -n '/^[0-9]/ p' hosts.txt
  913  sed -n '/^[0-9a-f]/ p' hosts.txt
  914  sed -n '/^[0-9a-f]{4}/ p' hosts.txt
  915  sed -n '/^[0-9a-f]/ p' hosts.txt
  916  sed -n 's/^[0-9a-f]/****/ p' hosts.txt
  917  sed -n 's/^[0-9a-f]/*/ p' hosts.txt
  918  sed -n 's/^[0-9a-f]*/*/ p' hosts.txt
  919  sed -n 's/^[0-9a-f]*/****/ p' hosts.txt
