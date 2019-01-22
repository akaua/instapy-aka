from instapy import InstaPy

session = InstaPy(username='', password='')

session.login()

###session.set_relationship_bounds(enabled=True,
###				 potency_ratio=None,
###				  delimit_by_numbers=True,
###				   max_followers=500,
###				    max_following=500,
###				     min_followers=45,
###				      min_following=77)


###session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
###session.set_do_follow(enabled=True, percentage=100)
###session.set_do_like(enabled=True, percentage=100)
###session.interact_user_followers(['naosouexposicao','naocontocalorias','nutricaosempressao','rizzo__marcia','desire.coelho','institutoaci','debemcommeuprato','sophiederam','nutnaiarabelmont','camilla_estima_nutricionista','comportamentoalimentar','garbindaiana','obarrigapositiva','futilidades','alexandrismos','bernardofala','eagoranutri'], amount=300, randomize=True)
#session.set_comments(["Cool", "Super!"])
#session.set_do_comment(enabled=True, percentage=80)

#session.follow_user_followers(['naosouexposicao','naocontocalorias','nutricaosempressao','rizzo__marcia','desire.coelho','institutoaci','debemcommeuprato','sophiederam','nutnaiarabelmont','camilla_estima_nutricionista','comportamentoalimentar','garbindaiana','obarrigapositiva','futilidades','alexandrismos','bernardofala','eagoranutri'], amount=50, sleep_delay=30, randomize=True, interact=False)
###session.interact_user_followers(['vanessajsilveira'], amount=20, randomize=True)
#session.follow_likers (['user1' , 'user2'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
#session.follow_commenters(['user1', 'user2', 'user3'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)

#custom_list = ["restricaonaoesolucao"]
#session.unfollow_users(amount=84, customList=(True, custom_list, "nonfollowers"), style="RANDOM", unfollow_after=55*60*60, sleep_delay=600)
#session.unfollow_users(amount=3000, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=60, sleep_delay=60)
session.unfollow_users(amount=1000, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
#session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=60, sleep_delay=655)
session.end()