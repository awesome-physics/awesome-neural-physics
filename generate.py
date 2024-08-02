import bibtexparser
from bibtexparser.bparser import BibTexParser

import util



def load_bibtex(file_path):
    with open(file_path, 'r') as bibtex_file:
        parser = BibTexParser()
        # parser.customization = homogenize_latex_encoding
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return bib_database.entries

def format_entry(entry):
    dict_entry={}
    dict_entry['title'] = entry.get('title', 'No title')
    dict_entry['author'] = entry.get('author', 'No author')
    dict_entry['year'] = entry.get('year', 'No year')
    dict_entry['link'] = entry.get('link', '')
    dict_entry['jabbr'] = util.get_jabbr(entry)
    label = entry.get('label', '')
    split_labels = [l.strip() for l in label.split(',')]
    dict_entry['label']=split_labels
    return dict_entry
    
    
    # return f"- **{title}** ({year}) by {author}. [Link]({link})" if link else f"- **{title}** ({year}) by {author}."

def generate_markdown(bib_entries, output_file):
    with open(output_file, 'w') as md_file:
        md_file.write(util.get_markdown_header())

        group_entry_dict={}
        label_color_dict={}

        group_entry_dict['fluid']=[]
        group_entry_dict['cloth']=[]
        group_entry_dict['softbody']=[]
        group_entry_dict['rigidbody']=[]
        group_entry_dict['multiphys']=[]
        group_entry_dict['survey']=[]
        
        # put into bib_entries
        for bib_entry in bib_entries:
            entry=format_entry(bib_entry)
            for label in entry['label']:
                if label in group_entry_dict.keys():
                    group_entry_dict[label].append(entry)
        
        # sort by year in dict
        for group_label, group_entries in group_entry_dict.items():
            group_entry_dict[group_label]=[v for v in sorted(group_entries, key=lambda entry: entry['year'])]

        # write out
        for group_label, group_entries in group_entry_dict.items():
            md_file.write("## "+group_label.title()+"\n\n")
            md_file.write("|Name|Info|Link|Label|\n")
            md_file.write("|---|---|---|---|\n")
            for entry in group_entries:
                labels=entry['label']
                label_str=''
                for label in labels:
                    label_str+='![][~'+label+']'
                    # add labels
                    if label not in label_color_dict.keys():
                        label_color_dict[label]=util.get_label_badge_link(label)
                
                md_file.write(f"|**{entry['title']}**| {entry['jabbr']} {entry['year']}| [Link]({entry['link']}) | {label_str}\n")
            # f"- **{title}** ({year}) by {author}. [Link]({link})" if link else f"- **{title}** ({year}) by {author}."
            md_file.write(f"\n\n")
        md_file.write(f"\n\n")

        md_file.write(util.get_markdown_footer())


        for label, color_code in label_color_dict.items():
            md_file.write(f"[~{label}]:{color_code}\n")

def main():
    input_bibtex = 'main.bib'
    output_markdown = 'README.md'
    
    bib_entries = load_bibtex(input_bibtex)
    generate_markdown(bib_entries, output_markdown)
    print(f"Awesome list generated and saved to {output_markdown}")

if __name__ == "__main__":
    main()