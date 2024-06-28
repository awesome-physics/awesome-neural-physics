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

def get_markdown_header():
    return ("# Awesome Neural Physics\n\n"
    "[This repository](https://github.com/awesome-physics/awesome-neural-physics) hosts a curated list of papers on **AI techniques for physics simulation** in computer graphics.\n\n"
    "If you find this list useful, please consider citing it and giving it a :star:. Feel free to share it with others!\n\n")

def get_markdown_footer():
    return ("## Citation\n\n"
    "If you find this repository helpful, please consider citing it!\n\n"
    "```@misc{wang2024awesomelist,\n"
    "title = {Awesome Neural Physics - A Curated List of Papers on AI Techniques for Physics Simulation in Computer Graphics},\n"
    "author = {Hui Wang},\n"
    "journal = {GitHub repository},\n"
    "url = {https://github.com/awesome-physics/awesome-neural-physics},\n"
    "year = {2023},\n"
    "}\n"
    "```\n")

jabbr_map={
    'ACM Transactions on Graphics (TOG)'.casefold():'TOG',
    'ACM Transactions on Graphics'.casefold():'TOG',
    'ACM Trans. Graph.'.casefold():'TOG',
    'IEEE Transactions on Visualization and Computer Graphics'.casefold():'TVCG',
    'Computer Graphics Forum'.casefold():'CGF',
    'Proceedings of the ACM on Computer Graphics and Interactive Techniques'.casefold():'PACMCGIT',
    'Proc. ACM Comput. Graph. Interact. Tech.'.casefold():'PACMCGIT',
    'Computational Visual Media'.casefold():'CVM',
    'Computer Animation and Virtual Worlds'.casefold():'CAVW',
    'Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)'.casefold():'CVPR',
    'Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition'.casefold():'CVPR',
    'The IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)'.casefold():'CVPR',
    'The IEEE/CVF Conference on Computer Vision and Pattern Recognition'.casefold():'CVPR',
    'Advances in Neural Information Processing Systems'.casefold():'NeurIPS',
    'Conference on Neural Information Processing Systems'.casefold():'NeurIPS',
    'Proceedings of the International Conference on Learning Representations'.casefold():'ICLR',
    'International Conference on Learning Representations'.casefold():'ICLR',
    'ICML'.casefold():'ICML',
    'International Conference on Machine Learning'.casefold():'ICML',
    'Proceedings of the AAAI Conference on Artificial Intelligence'.casefold():'AAAI',
    'Proceedings of the european conference on computer vision (eccv)'.casefold():'ECCV',
    'European Conference on Computer Vision'.casefold():'ECCV',
    'Proceedings of the IEEE/CVF International Conference on Computer Vision'.casefold():'ICCV',
    'Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)'.casefold():'ICRA',
    'IEEE International Conference on Robotics and Automation (ICRA)'.casefold():'ICRA',
    'International Conference on Robotics and Automation (ICRA)'.casefold():'ICRA'
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
