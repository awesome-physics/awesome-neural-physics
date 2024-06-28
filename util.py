import matplotlib.colors as mcolors

def get_jabbr(entry):
    if entry['ENTRYTYPE'].lower()=='article':
        return _jabbr_mapping(entry['journal'])
    if entry['ENTRYTYPE'].lower()=='inproceedings':
        return _jabbr_mapping(entry['booktitle'])
    if entry['ENTRYTYPE'].lower()=='misc':
        return ''


colors=list(mcolors.TABLEAU_COLORS.values())

def get_label_badge_link(label):
    color_code=colors[ord(label[0])%len(colors)][1:]
    return f"https://img.shields.io/badge/-{label}-{color_code}.svg"

class CaseInsensitiveDict(dict):
    """Case-insensitive dictionary implementation."""

    def __getitem__(self, key):
        return dict.__getitem__(self, key.casefold())

    def __setitem__(self, key, value):
        return dict.__setitem__(self, key.casefold(), value)

    def __delitem__(self, key):
        return dict.__delitem__(self, key.casefold())

jabbr_map={
    'ACM Transactions on Graphics (TOG)'.casefold():'TOG',
    'ACM Transactions on Graphics'.casefold():'TOG',
    'ACM Trans. Graph.'.casefold():'TOG',
    'IEEE Transactions on Visualization and Computer Graphics'.casefold():'TVCG',
    'Computer Graphics Forum'.casefold():'CGF',
    'Computer Animation and Virtual Worlds'.casefold():'CAVW',
    'Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)'.casefold():'CVPR',
    'Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition'.casefold():'CVPR',
    'The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)'.casefold():'CVPR',
    'The IEEE/CVF Conference on Computer Vision and Pattern Recognition'.casefold():'CVPR',
    'Advances in Neural Information Processing Systems'.casefold():'NeurIPS',
    'Conference on Neural Information Processing Systems'.casefold():'NeurIPS',
    'International Conference on Learning Representations'.casefold():'ICLR',
    'ICML'.casefold():'ICML',
    'International Conference on Machine Learning'.casefold():'ICML',
    'Proceedings of the AAAI Conference on Artificial Intelligence'.casefold():'AAAI',
    'Proceedings of the european conference on computer vision (eccv)'.casefold():'ECCV',
    'European Conference on Computer Vision'.casefold():'ECCV',
    'Proceedings of the IEEE/CVF International Conference on Computer Vision'.casefold():'ICCV',
    'Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)'.casefold():'ICRA'

}
def _jabbr_mapping(j):
    if j.casefold() in jabbr_map:
        return jabbr_map[j.casefold()]
    elif j.casefold().startswith('arxiv'):
        return 'Arxiv'
    elif 'siggraph asia' in j.casefold():
        return 'Siggraph Asia'
    elif 'siggraph' in j.casefold():
        return 'Siggraph'
    else:
        return ''
        print('find no ',j,'in our mapping')