# from apiclient.discovery import build
# from apiclient.errors import HttpError
# from oauth2client.tools import argparser
# # import csv, os

# # csv_reader = csv.reader(open(os.getcwd() + '/youtube_credential.csv'), delimiter=',')
# # DEVELOPER_KEY = next(csv_reader)[0]
# DEVELOPER_KEY = 'AIzaSyDStmAssbrGPfK7RyQEdAd8xxl5b7TtlIg'
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"

# youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

# def youtubeSearch(query, max_results=3,order="relevance", token=None, location=None, location_radius=None):
#     search_response = youtube.search().list(
#     q=query,
#     type="video",
#     pageToken=token,
#     order = order,
#     part="id,snippet",
#     maxResults=max_results,
#     location=location,
#     locationRadius=location_radius).execute()
#     items = search_response['items'] #50 "items"

#     return search_response

# def storeResults(response):
#     title = []
#     channelId = []
#     channelTitle = []
#     categoryId = []
#     videoId = []
#     viewCount = []
#     likeCount = []
#     dislikeCount = []
#     commentCount = []
#     favoriteCount = []
#     category = []
#     tags = []
#     videos = []
#     publishDate = []
    
#     for search_result in response.get("items", []):
#         if search_result["id"]["kind"] == "youtube#video":

#             title.append(search_result['snippet']['title'])
#             videoId.append(search_result['id']['videoId'])

#             stats = youtube.videos().list(
#                 part='statistics, snippet',
#                 id=search_result['id']['videoId']).execute()
            
#             channelId.append(stats['items'][0]['snippet']['channelId']) 
#             channelTitle.append(stats['items'][0]['snippet']['channelTitle']) 
#             categoryId.append(stats['items'][0]['snippet']['categoryId']) 
#             favoriteCount.append(stats['items'][0]['statistics']['favoriteCount'])
#             viewCount.append(stats['items'][0]['statistics']['viewCount'])
#             publishDate.append(stats['items'][0]['snippet']['publishedAt'])
#             try:
#                 likeCount.append(stats['items'][0]['statistics']['likeCount'])
#             except:
#                 likeCount.append("Not available")
                
#             try:
#                 dislikeCount.append(stats['items'][0]['statistics']['dislikeCount'])     
#             except:
#                 dislikeCount.append("Not available")

#             if 'commentCount' in stats['items'][0]['statistics'].keys():
#                 commentCount.append(stats['items'][0]['statistics']['commentCount'])
#             else:
#                 commentCount.append(0)
         
#             if 'tags' in stats['items'][0]['snippet'].keys():
#                 tags.append(stats['items'][0]['snippet']['tags'])
#             else:
#                 tags.append("No Tags")
                
#     youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,
#                     'categoryId':categoryId,'title':title,'videoId':videoId,
#                     'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,
#                     'commentCount':commentCount,'favoriteCount':favoriteCount, 'publishDate': publishDate}
 
#     return youtube_dict


# # #Input query
# # print("Please input your search query")
# # q=input()
# # #Run YouTube Search
# # response = youtubeSearch(q)
# # results = storeResults(response)
# # #Display result titles
# # # print("Top 3 results are: \n {0}, ({1}), \n {2}, ({3}),\n {4}, ({5})".format(results['title'][0],results['tags'][0],
# # #                                                                              results['title'][1],results['tags'][1],
# # #                                                                              results['title'][2],results['tags'][2]))

# # concat = results['tags'][0] + results['tags'][1] + results['tags'][2]
# # print(set(concat))