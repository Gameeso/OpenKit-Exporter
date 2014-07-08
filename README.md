OpenKit-Exporter
================

Allow users to export as much data from OpenKit as possible!

See [http://gameeso.com/openkit-notes/](http://gameeso.com/openkit-notes/) for more info

#Hi Guys
This is the first try for making a tool to export your openkit data.
Currently it's capable of exporting the following:

- Export leaderboards
- **Export all score inside each leaderboard!**	This might take some time depending on how much data you've got :)

- Export users that made the scores

See sample [here](#example-exported-file)

Upon giving your app key and secret, the tool will store the above mentioned data in a json file inside folder of this script. **Be sure to keep it safe**

#Yes! Give it to me!

1. Start with cloning this repo to a folder on your computer.
2. cd to where you cloned this repo
3. Install dependencies			sudo pip install -r requirements.txt
4. Now run the script		python main.py
5. Follow along the instructions. Please be sure to use your openkit app key and secret of the game you want to export.   When done, **keep your data json safe!!!** it's yours now.

#If you like what I've done
Please consider a donation! See [http://gameeso.com/#donation](http://gameeso.com/#donation) for more info.

Also, any contribution is greatly appreciated!

#Faq

- **What can I do with the data?**

	In the near future you can use this data to import into Gameeso at your desire. Currently I (or we when the community grows :)) do not have a feature to import your data yet into Gameeso
	
- **This doenst export everything!**

	I know, it's hard to export from OpenKit using just whatever their server exposes. This tool puts the pieces back together like a puzzle.
	I'm propably going to update the script every once in a while if I find new ways to export more **be sure to follow this project if you want to be up to date!**
	
- **Why export my data if I cant do anything with it?**

	**OpenKit shuts down on sept 1.** This is not about Gameeso, this is about your data on OpenKit. The tool I made is some kind of "insurance-policy" to keep your data even if Gameeso will never launch.
	
- **How do I get my data?**
	
	The data is pulled using a script from the offical openkit servers, stored in a custom JSON format (not related to SQL) for easy re-import once we get to that point.
	
#Example exported file

	{
	    "leaderboards": [
	        {
	            "app_id": 1,
	            "created_at": "2014-07-06T15:17:27.000Z",
	            "gamecenter_id": "",
	            "gpg_id": "",
	            "icon_content_type": null,
	            "icon_file_name": null,
	            "icon_file_size": null,
	            "icon_updated_at": null,
	            "icon_url": "http://api.gameeso.comhttps://ok-shared.s3-us-west-2.amazonaws.com/leaderboard_icon.png",
	            "id": 1,
	            "name": "Poopie!",
	            "player_count": 1,
	            "priority": 100,
	            "scores": [
	                {
	                    "created_at": "2014-07-06T21:18:44.000Z",
	                    "display_string": null,
	                    "id": 3,
	                    "is_users_best": true,
	                    "leaderboard_id": 1,
	                    "meta_doc_url": null,
	                    "metadata": 0,
	                    "rank": 1,
	                    "user_id": 1,
	                    "value": 30
	                }
	            ],
	            "sort_type": "HighValue",
	            "updated_at": "2014-07-06T15:17:27.000Z"
	        }
	    ],
	    "users": [
	        {
	            "created_at": "2014-07-06T21:17:01.000Z",
	            "custom_id": null,
	            "developer_id": 1,
	            "fb_id": "100002273765146",
	            "gamecenter_id": null,
	            "google_id": null,
	            "id": 1,
	            "nick": "Peter Willemsen",
	            "twitter_id": null,
	            "updated_at": "2014-07-06T21:17:01.000Z"
	        }
	    ]
	}
