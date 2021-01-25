import math
import sys
import MeCab

from typing import Dict, List, Union

# MeCab追加辞書
DIC_TOKENIZER = '/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'


class NaiveBayes:
    """ ベイジアンフィルタ（ナイーブベイズ）
        単語がカテゴリに属する確率（生起確率）による分類
    """
    def __init__(self):
        self.words = set()  # 抽出した単語をすべて登録
        self.n_word_in_cat = {}  # カテゴリごとの単語出現回数を登録
        self.n_cat = {}  # カテゴリの出現回数を登録

    # 単語出現回数をカテゴリと共に登録
    def countup_word(self, word: str, cat: str) -> None:
        self.n_word_in_cat.setdefault(cat, {})
        self.n_word_in_cat[cat].setdefault(word, 0)
        self.n_word_in_cat[cat][word] += 1
        self.words.add(word)

    # カテゴリ出現回数を登録
    def countup_cat(self, cat: str) -> None:
        self.n_cat.setdefault(cat, 0)
        self.n_cat[cat] += 1

    # 文章とカテゴリで学習（訓練）
    def fit(self, text: str, cat: str) -> None:
        words_in_text = self.word_tokenize(text)
        for word in words_in_text:
            self.countup_word(word, cat)
        self.countup_cat(cat)

    # カテゴリの生起確率を取得
    def get_prob(self, cat: str) -> float:
        return float(self.n_cat[cat]) / sum(self.n_cat.values())

    # 単語がカテゴリの中にある確率を取得
    def get_inword_prob(self, word: str, cat: str) -> float:
        # 加算スムージング
        n_words = float(self.n_word_in_cat[cat][word] if word in self.n_word_in_cat[cat] else 0) + 1
        n_all = sum(self.n_word_in_cat[cat].values()) + len(self.words) * 1

        return n_words / n_all

    # 確率値（スコア）を取得
    def score(self, word_list: List[str], cat: str) -> float:
        score = math.log(self.get_prob(cat))
        for word in word_list:
            score += math.log(self.get_inword_prob(word, cat))
        return score

    # カテゴリの最大確率値を決定（予測）
    def predict(self, text: str) -> Union[str, list]:
        best_cat = None
        max_score = -sys.maxsize
        word_list = self.word_tokenize(text)
        score_list = []

        for cat in self.n_cat.keys():
            score = self.score(word_list, cat)
            score_list.append((cat, score))
            if score > max_score:
                max_score = score
                best_cat = cat

        return best_cat, score_list

    # 形態素解析
    def word_tokenize(self, text: str) -> List[str]:
        tokenizer = MeCab.Tagger('-d {}'.format(DIC_TOKENIZER))
        nodes = tokenizer.parseToNode(text)
        noun_list = []

        # 品詞が名詞のみ抽出
        while nodes:
            word_class = nodes.feature.split(',')
            if word_class[0] == '名詞':
                noun_list.append(nodes.surface)
            nodes = nodes.next

        return noun_list

    @property
    def words(self) -> List[str]:
        return self.words

    @property
    def n_cat(self) -> Dict:
        return self.n_cat

    @property
    def n_word_in_cat(self) -> Dict:
        return self.n_word_in_cat
