#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/6/28 15:37
# Author : lixingyun
# Description :
# admin_cases = ['/channel/getChannelList']
# other_links = ['#', '/eventTreasures/index', '/treasureSends/index','/guess/index','/guessuser/index']
#
# ret = requests.get(domain_admin, cookies=ADMIN_COOKIES).text
# links = etree.HTML(ret).xpath('//a')
# for link in links:
#     href = link.get('href')
#     if href not in other_links:
#         admin_cases.append(href.strip()) # 去除首尾空额
admin_urls = [
    '/channel/channelListManage',
    '/channel/getChannelList',
    '/outlink/stream',
    '/channel/popularity',
    '/channel/popularityList',
    '/userspeak/index',
    '/tape/index',
    '/tape/pageList',
    '/channelevent/activeIndex',
    '/channelevent/activeList',
    '/userInfo/index',
    '/memberbadge/index',
    '/channel/speechLimitMange',
    '/channel/speechLimitList',
    '/channelwhites/index',
    '/channelwhites/getlist',
    '/roomnumbers/index',
    '/roomnumbers/getlist',
    '/channel/channelHidManage',
    '/channel/getChannelHidList',
    '/robotchat/index',
    '/robotchat/chat_list',
    '/reorder/channel',
    '/reorder/pageList',
    '/anchorRank/index',
    '/anchorRank/grid',
    '/anchorGiftRank/index',
    '/anchorGiftRank/grid',
    '/anchorRankSource/index',
    '/anchorRankSource/grid',
    '/recommend/channel',
    '/recommend/channelList',
    '/advert/index',
    '/advert/advertList',
    '/channelRecs/index',
    '/channelRecs/getlist',
    '/recommend/match',
    '/recommend/matchList',
    '/theme/index',
    '/theme/themeList',
    '/MobileActive/activeIndex',
    '/mobileActive/activeList',
    '/Reclink/index',
    '/reclink/advertList',
    '/shareactive/activeIndex',
    '/shareactive/activeList',
    '/VersionCommit/index',
    '/autoReplayManage/index',
    '/autoReplayManage/getlist',
    '/mobilefunctions/index',
    '/mobilefunctions/functionList'
    '/advert/advertCate',
    '/advert/advertCatelist',
    '/createtab/index',
    '/createtab/tabList',
    '/tempIcons',
    '/guessuser/index',
    '/adminsubscribe/index',
    '/adminsubscribe/adminSubscribeList',
    '/message/index',
    '/message/messageList',
    '/wechattype/index',
    '/wechattype/getwechattypelist',
    '/wechatanchor/index',
    '/wechatanchor/WechatAnchorList',
    '/connectmicAuth/index',
    '/ConnectmicAuth/authList',
    '/channel/closure',
    '/channel/closureList',
    '/channel/killStream',
    '/channel/killChannelList',
    '/user/blackmenu',
    '/user/userBlackMenuList',
    '/report/reportUser',
    '/report/reportUserList',
    '/gag/index',
    '/gag/gagList',
    '/cdn/cdnList',
    '/cdn/getCdnList',
    '/monitor/index',
    '/monitor/getChannels',
    '/channel/shumei',
    '/channel/shuMeiList',
    '/CheckImgLog/checkchannel',
    '/CheckImgLog/channelList',
    '/feedback/index',
    '/feedback/feedList',
    '/report/index',
    '/report/reportList',
    '/anchor/lists',
    '/bankcard/index',
    '/bag/index',
    '/bag/grid',
    '/bag/sendRecord',
    '/bag/sendRecordGrid',
    '/bag/useRecord',
    '/bag/useRecordGrid',
    '/noble/send',
    '/noble/sendRecordGrid',
    '/bannedgift/showaddlist',
    '/bannedgift/getBannedList',
    '/treasureSends/index',
    '/treasureSends/getlist',
    '/specialNoble/send',
    '/specialNoble/sendRecordGrid',
    '/simulatelogin/index',
    '/incremoney/index',
    '/incremoney/getloglist',
    '/memberbadge/showaddlist',
    '/memberbadge/getMemberBadgeAddLog',
    '/whitelist',
    '/djgoods/index',
    '/djgoods/giveLists',
    '/news/getList',
    '/news/jsonNewsList',
    '/game/gameListManage',
    '/game/getGamelList',
    '/gamecollection/gameCollectionManage',
    '/gamecollection/getCollectionList',
    '/reccattype/recCatTypeManage',
    '/reccattype/getReccattypeList',
    '/reccattypecont/recCatTypeContManage',
    '/reccattypecont/getReccattypeContList',
    '/reccatcontpos/recCatContPosManage',
    '/reccatcontpos/getReccatContPosList',
    '/gift',
    '/gift/giftList',
    '/sharecontent/activeIndex',
    '/sharecontent/activeList',
    '/topnews/index',
    '/topnews/newsList',
    '/mobiletab/index',
    '/PlaygroundItem/index',
    '/PlaygroundItem/getList',
    '/channellabel/labelListManage',
    '/channellabel/getLabelList',
    '/badgemanage/index',
    '/badgemanage/getBadgeList',
    '/Weekstargift/index',
    '/help/index',
    '/help/jsonHelpList',
    '/hotwordssearch/index',
    '/hotwordssearch/wordsList',
    '/h5links/index',
    '/h5links/geth5links',
    '/hotwordssearch/channelIndex',
    '/hotwordssearch/channellist',
    '/lotterys/attach',
    '/lotterys/grid',
    '/lotterys/monitor',
    '/lotterys/record',
    '/lotterys/recordgrid',
    '/video/index',
    '/video/pageList',
    '/guessnew/team',
    '/guessnew/team_list',
    '/guessnew/match',
    '/guessnew/match_list',
    '/guessnew/periods',
    '/guessnew/period_list',
    '/guessnew/orders',
    '/guessnew/order_list',
    '/guessnew/user',
    '/guessnew/room',
    '/guessnew/room_list',
    '/award/index',
    '/exchangeshop/index',
    '/room/index',
    '/bankcash/index',
    '/smallgame/index',
    '/smallgame/game_list',
    '/smallgame/room',
    '/smallgame/room_list',
    '/smallgame/period',
    '/smallgame/period_list',
    '/smallgame/order',
    '/smallgame/order_list',
    '/smallgame/user',
    '/badgecategory/index',
    '/badgecategory/grid',
    '/advertmanage/index',
    '/event/eventList',
    '/event/getEventList',
    '/event/teamList',
    '/event/getTeamList',
    '/event/racesList',
    '/event/getRacesList',
    '/advertevent/index',
    '/advertevent/advertList',
    '/eventbrand/index',
    '/eventbrand/getEventBrandList',
    '/vdemand/index',
    '/vdemand/getDemandList',
    '/eventTreasures/index',
    '/eventTreasures/getlist',
    '/special/index',
    '/special/specialList',
]

admin_cases = []
for url in admin_urls:
    admin_cases.append(tuple([url]))

# print(admin_cases)