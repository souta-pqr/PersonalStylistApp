import datetime

def get_personalized_recommendation(style, user_profile):
    base_recommendation = get_style_recommendation(style)
    
    if user_profile.body_type == 'plus_size':
        base_recommendation += " プラスサイズの方に似合うゆったりとしたシルエットを選びましょう。"
    
    if 'casual' in user_profile.preferences:
        base_recommendation += " あなたの好みに合わせて、カジュアルな要素を取り入れるのもおすすめです。"
    
    return base_recommendation

def get_style_recommendation(style):
    recommendations = {
        'casual': "快適でリラックスしたカジュアルウェアを選びましょう。ジーンズとTシャツの組み合わせがおすすめです。",
        'formal': "フォーマルな場面に適した洗練されたスタイルを。スーツやドレスシャツを考えてみてはいかがでしょうか。",
        'sporty': "アクティブなライフスタイルに合わせて、機能的でスタイリッシュなスポーツウェアを。",
        'bohemian': "自由奔放で芸術的な雰囲気を演出する、ゆったりとしたシルエットや民族調のプリントを取り入れてみましょう。",
        'preppy': "クラシックでエレガントな雰囲気を。ポロシャツやチノパンなどのアイテムがおすすめです。"
    }
    return recommendations.get(style, "スタイルに合わせたおすすめのファッションを探してみましょう。")

def adjust_recommendation_for_season_and_occasion(recommendation, season, occasion):
    season_adjustments = {
        'spring': "軽めのアウターやパステルカラーを取り入れると季節感が出ます。",
        'summer': "涼しげな素材や明るい色使いで夏らしさを演出しましょう。",
        'autumn': "レイヤードスタイルや温かみのある色調がおすすめです。",
        'winter': "厚手のアウターや暖かい素材を選びましょう。"
    }
    
    occasion_adjustments = {
        'work': "きちんと感のあるアイテムを選び、清潔感を意識しましょう。",
        'party': "アクセサリーやドレスアップアイテムでフォーマル感を出しましょう。",
        'casual': "快適さを重視しつつ、トレンドアイテムを取り入れるのもおすすめです。"
    }
    
    return f"{recommendation} {season_adjustments[season]} {occasion_adjustments[occasion]}"

def get_item_specific_recommendation(item):
    item_recommendations = {
        'shirt': "体型に合わせたフィット感のあるシャツを選びましょう。",
        'pants': "ラインが美しいパンツを選び、全体のバランスを整えましょう。",
        'dress': "場面に応じた適切な丈とシルエットのドレスを選びましょう。",
        'jacket': "季節に合わせた素材と、全体の色調に合うジャケットを選びましょう。"
    }
    return item_recommendations.get(item, "このアイテムに合わせたコーディネートを考えてみましょう。")