comments_list = "attractive,pretty,handsome,good-looking,nice-looking,pleasing,alluring,prepossessing,lovely,charming,delightful,appealing,engaging,winsome,ravishing,gorgeous,heavenly,stunning,arresting,glamorous,irresistible,bewitching,beguiling,graceful,elegant,exquisite,aesthetic,artistic,decorative,magnificent,amazing,astonishing,staggering,shocking,surprising,breathtaking,striking,impressive,bewildering,stunning,stupefying,unnerving,unsettling,disturbing,disquieting,awe-inspiring,remarkable,notable,noteworthy,extraordinary,outstanding,incredible,unbelievable,phenomenal"
new_comments_list = []
comments_list = comments_list.split(",")
vowels = ['a', 'e', 'i', 'o', 'u']
for comment in comments_list:
	if comment[0] in vowels:
		connector = "an"
	else:
		connector = "a"
	comment = f"What {connector} {comment} picture!"
	new_comments_list.append(comment)

print(new_comments_list)
