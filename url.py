import webbrowsor
url={}
class Short:
    global url
    id=100
    def shortenurl(self,original_url):
        if original_url in self.url:
            id=self.url[original_url]
        else:
            self.url[original_url]=self.id
            self.id+=1
            return self.id
        def get_key(val): 

            for key, value in url.items(): 

                if val == value: 

                    return key 
u=input("Enter the url:")
u=Short()
n=u.shortenurl(u)
str1="short_url.com/"+str(n)
print("Short url is:",str1)
webbrowsor.open(get_key(str1))

