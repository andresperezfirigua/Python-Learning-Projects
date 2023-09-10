from instagrambot import InstagramBot

account = 'Account'

instaBot = InstagramBot()
instaBot.login()
followers_list = instaBot.find_followers(account)
instaBot.follow(followers_list)

instaBot.driver.quit()
