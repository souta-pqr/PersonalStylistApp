def get_personalized_recommendation(style, detected_items, user_profile):
    base_recommendation = get_style_recommendation(style)
    
    if user_profile.body_type == 'plus_size':
        base_recommendation += " ゆったりとしたシルエットで体型を美しく見せることができます。"
    
    if 'casual' in user_profile.preferences:
        base_recommendation += " カジュアルテイストを取り入れることで、より親しみやすい印象に仕上がります。"
    
    # 検出されたアイテムに基づく推奨を追加
    for item in detected_items:
        base_recommendation += f" {item}については、"
        if item == 'person':
            base_recommendation += "全身のバランスを整えることで、より洗練された印象になります。"
        elif item in ['shirt', 'top']:
            base_recommendation += "上半身のシルエットを整えることで、スタイルアップが期待できます。"
        elif item in ['pants', 'skirt']:
            base_recommendation += "下半身のラインを意識することで、全体的なバランスが良くなります。"
    
    return base_recommendation

def get_style_recommendation(style):
    recommendations = {
        'casual': "快適性を重視したカジュアルスタイルがおすすめです。デニムとTシャツの組み合わせで、こなれた雰囲気を演出できます。",
        'formal': "品格のある装いで、正式な場面に相応しい印象に。スーツやドレスシャツで、洗練された雰囲気を演出しましょう。",
        'sporty': "機能性とデザイン性を兼ね備えたスポーツウェアで、アクティブな印象を演出します。",
        'bohemian': "ゆったりとしたシルエットやエスニックプリントで、自由な雰囲気を表現してみましょう。",
        'preppy': "清潔感のあるアイテムで知的な印象に。ポロシャツやチノパンで、品のある着こなしを実現できます。"
    }
    return recommendations.get(style, "あなたの個性を活かしたスタイリングをご提案いたします。")

def adjust_recommendation_for_season_and_occasion(recommendation, season, occasion):
    season_adjustments = {
        'spring': "春らしい軽やかな装いには、薄手のアウターやパステルカラーがおすすめです。",
        'summer': "夏の爽やかさを演出する涼しげな素材選びと、明るい色使いを心がけましょう。",
        'autumn': "秋の装いには、重ね着とあたたかみのある色使いがぴったりです。",
        'winter': "冬は保温性の高い素材を選び、暖かさと洗練さを両立させましょう。"
    }
    
    occasion_adjustments = {
        'work': "ビジネスシーンに相応しい、清潔感とプロフェッショナルな印象を大切にしましょう。",
        'party': "パーティーシーンでは、アクセサリーや華やかなアイテムで特別感を演出します。",
        'casual': "快適さを重視しながら、トレンド要素を取り入れることで、おしゃれ度がアップします。"
    }
    
    return f"{recommendation} {season_adjustments[season]} {occasion_adjustments[occasion]}"