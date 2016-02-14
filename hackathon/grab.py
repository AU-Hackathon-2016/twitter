'''
Created on Feb 13, 2016

@author: yuanqi
'''
"""
Use Twitter API to grab user information from list of organizations; 
export text file
Uses Twython module to access Twitter API
"""

from twython import Twython
import json
import urllib2
import base64

def spiderInfo(name,limit):
    resultInfo=[]
    index = 0
    c=0
    if limit==0:
        limit=5
    t = Twython(app_key='6JGtb2KvWbCNiFL2yxM4tsf3X', 
        app_secret='8PKemZoO4iM5JMfDxxCdpstPjbJBUqqVWwTkZlULoMqJULSO5V',
        oauth_token='704548355-t91wJGga1YdvwimCgoOTmaDE9wU3gpK4SojmATwz',
        oauth_token_secret='EdDeMHy5cvE2SYhAE2bRsartr4iAkYMo34TZzCj2HeVaj')
    
    while c<limit:
        res=t.search_users(q=name,page=index,count=5)
        length=len(res)
        for content in res:
            dict={}
            dict['profile_image_url']=encodeImage(content['profile_image_url'])
            dict['location']=content['location']
            dict['name']= content['name']
            dict['screen_name']=content['screen_name']
#            print dict['name']
            dict['lang']=content['lang']
            dict['friends_count']=content['friends_count']
            dict['time_zone']= content['time_zone']
            dict['description']=content['description']
            dict['favourites_count'] =content['favourites_count']
            dict['followers_count'] =content['followers_count']
            resultInfo.append(dict)
            c+=1
            if c==limit:
                return resultInfo
        if length<5:
            return resultInfo
        index+=1
    return resultInfo

def encodeImage(url):
    if url=='': 
        return
    img = urllib2.urlopen(url).read()
    encoded = base64.b64encode(img)
    return encoded
    

#print len(spiderInfo('ryan',200))   
