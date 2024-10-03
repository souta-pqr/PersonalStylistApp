from PIL import Image
import torch

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    return image

def get_style_recommendation(style):
    # この関数は、スタイルに基づいて推奨事項を生成します
    # 実際のアプリケーションでは、より洗練されたロジックを実装する必要があります
    recommendations = {
        'casual': "快適でリラックスしたカジュアルウェアを選びましょう。ジーンズとTシャツの組み合わせがおすすめです。",
        'formal': "フォーマルな場面に適した洗練されたスタイルを。スーツやドレスシャツを考えてみてはいかがでしょうか。",
        'sporty': "アクティブなライフスタイルに合わせて、機能的でスタイリッシュなスポーツウェアを。",
        'bohemian': "自由奔放で芸術的な雰囲気を演出する、ゆったりとしたシルエットや民族調のプリントを取り入れてみましょう。",
        'preppy': "クラシックでエレガントな雰囲気を。ポロシャツやチノパンなどのアイテムがおすすめです。"
    }
    return recommendations.get(style, "スタイルに合わせたおすすめのファッションを探してみましょう。")