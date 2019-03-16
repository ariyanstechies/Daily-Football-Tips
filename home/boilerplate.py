#! this is where huge comparison goes b4 data is insterted into database
from home.statArena import stat_arena
from home.zulubet import zulu_procedure
from home.models import AllGames, Featured, TipGG, Over15, Over25, Over35
from difflib import SequenceMatcher

def boiler(zulu_page, page, page2, today):
    zulu_arr = zulu_procedure(zulu_page, today)
    stat_arr_orign = stat_arena(page, today)
    stat_arr = stat_arena(page, today)
    featured_arr = stat_arena(page2, today)
    print("Games One length: %s\nGames two length: %s" % (len(zulu_arr), len(stat_arr)))
    success_compr = []
    status = 0
    for each2 in range(len(stat_arr)):
        # print("Outer Loop remaining %d" % len(stat_arr))
        # print("each2 in outer loop %s" % each2)
        for each in range(len(zulu_arr)):
            # print("each in inner loop %s" % each)
            s = SequenceMatcher(None, zulu_arr[each][4], stat_arr[each2][4])
            if s.ratio() > 0.5:
                if SequenceMatcher(None, zulu_arr[each][1], stat_arr[each2][1]).ratio() > 0.6:
                    # print("%s / %s  Efficiency %s" % (zulu_arr[each][4], stat_arr[each2][3], SequenceMatcher(None, zulu_arr[each][4], stat_arr[each2][3]).ratio()))
                    if stat_arr[each2][3].strip() != "":
                        res = stat_arr[each2][3]
                    else:
                        if stat_arr[each2][3] == "":
                            res = zulu_arr[each][3]
                        else:
                            res = stat_arr[each2][3]
                    success_compr.append([zulu_arr[each][0],zulu_arr[each][1],"%s,%s" % (zulu_arr[each][2],stat_arr[each2][2]),res,stat_arr[each2][4],zulu_arr[each][5], zulu_arr[each][6], stat_arr[each2][7]])
                    # print("index for each %d" % each)
                    del zulu_arr[each]
                    ##                    zulu_arr[each][4]+" looks like \n
                    # print("index for each2 %d" % each2)
                    status = 1
                    break
                else:
                    status=0
            else:
                status = 0
        # print("Counter Level %d" % count)
        # print("status %d" % status)
        if status == 1:
            # print("index for each2 outer %d" % each2)
            stat_arr[each2] = 'remv'
            status = 0
        # print("Inner Loop remaining %d" % len(zulu_arr))
    print("Games that could be compared are %d out of %d" % (len(success_compr), len(stat_arr)))
    stat_arr_clean = [x for x in stat_arr if x!="remv"]
    print("Games one length unmatched: %s\nGames two length unmatched: %s" %(len(zulu_arr), len(stat_arr_clean)))
    combined_games = zulu_arr + success_compr
    # + stat_arr_clean removed
    # for allgames
    for each in combined_games:
        obj, created = AllGames.objects.update_or_create(
            teams=each[4],
            defaults={
                'match_date': each[0],
                'time': each[1],
                'teams': each[4],
                'tip': each[2],
                'tip_odd': each[5],
                'ft_results': each[3],
                'outcome_text': each[6],
            })
    print("allgames done")
    # for tipGG
    for each in stat_arr_orign:
        if each[7]:
            TipGG.objects.update_or_create(
                teams=each[4],
                defaults={
                    'match_date': each[0],
                    'time': each[1],
                    'teams': each[4],
                    'tip_gg': each[7],
                    'tip_gg_odd': each[5],
                    'ft_results': each[3],
                    'outcome_text': each[6]
                })
        # for Over15
        if each[8]:
            Over15.objects.update_or_create(
                teams=each[4],
                defaults={
                    'match_date': each[0],
                    'time': each[1],
                    'teams': each[4],
                    'tip_ov': each[8],
                    'tip_ov_odd': each[5],
                    'ft_results': each[3],
                    'outcome_text': each[6]
                })
        # for Over25:
        if each[9]:
            Over25.objects.update_or_create(
                teams=each[4],
                defaults={
                    'match_date': each[0],
                    'time': each[1],
                    'teams': each[4],
                    'tip_ov': each[9],
                    'tip_ov_odd': each[5],
                    'ft_results': each[3],
                    'outcome_text': each[6]
                })
        # for Over35
        if each[10]:
            Over35.objects.update_or_create(
                teams=each[4],
                defaults={
                    'match_date': each[0],
                    'time': each[1],
                    'teams': each[4],
                    'tip_ov': each[10],
                    'tip_ov_odd': each[5],
                    'ft_results': each[3],
                    'outcome_text': each[6]
                })
    print("Big Thing done")
    # for Featured Games
    for each in featured_arr:
        Featured.objects.update_or_create(
            teams=each[4],
            defaults={
                'match_date': each[0],
                'time': each[1],
                'teams': each[4],
                'tip': each[2],
                'tip_odd': each[5],
                'ft_results': each[3],
                'outcome_text': each[6]
            })
    print("Featured Games done")
