#To test hitString on different languages

from tld import get_tld
import lolmax

url = raw_input("Enter : ")

print lolmax.hitString(8, url)

'''Testing on Chinese Websites
1. qq.com - O/P - unicode characters - Nothing relevan found. Abort.
2. http://www.sina.com.cn/ - Same
3. http://www.163.com/ - Same
4. http://www.sohu.com/ - Same
5. https://world.taobao.com/ - Same
6. http://weibo.com/login.php - Same


Not useful for language other than english
'''

