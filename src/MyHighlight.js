// const CustomHighlight = ({ children, highlightIndex }) => (
//     'strong'
//  );

import React from 'react';



const MyHighlight = ({text = '', highlightlist = []}) => {


var highlight = highlightlist; // redundant 
 

var updateText='',
    tlk='',
    color='#FFFF00',
    d = '</span>',
    b = ''

    if (text !== ''){
        updateText = text;
        tlk = text.toLowerCase()

    for (let i = 0; i<highlight.length; i++ ){
      

      var indexT = tlk.indexOf(highlight[i].original.toLowerCase());
     

      // console.log("detecting:",highlight[i].replaceAll("[^a-zA-Z]+", ""))

      var lengthT = highlight[i].original.length

      if (indexT > -1){
        b = `<span data-tip data-for=${highlight[i].id} style="background-color:${color}">`
        d = `</span>`
      
        updateText = [updateText.slice(0, indexT), b, updateText.slice(indexT,indexT+lengthT),d, updateText.slice(indexT+lengthT)].join('')
        tlk = updateText.toLowerCase()

    }

    }}
    
    return (
      <React.Fragment>
      <div className="result-title secondary-title">
        <h3 className="m-blockLinkList__title">Result</h3></div>
      <div className="result-text" dangerouslySetInnerHTML={{__html: updateText}}></div>
      </React.Fragment>
    )

 }

export default MyHighlight;