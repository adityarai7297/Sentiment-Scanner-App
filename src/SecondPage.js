import React from 'react';
import MyHighlight from './MyHighlight';
import MyToolTip from './MyToolTip';
import MySummary from './MySummary';
import alex from 'alex';


export default function SecondPage({currentResultStr, setCurrentResult}){

    function getAlex(t){
        var alist = []
        var text = t.replace(/(master.*?s.*?de)/gi, '')

        console.log('after preprocessing', text)

          alex.text(text).messages.map((m)=>{ 
              
              const entry = {
                  id: 'alex'+ m.column,
                  category: 'insensitive, inconsiderate writing',
                  reason: m.reason,
                  original:m.actual
              }
              alist.push(entry)
              })
          
          console.log("reformatting result from alex", alist)
          return alist
    }
    
    var currentResult = ''
    

    if (currentResultStr !== ''){
        
        currentResult = JSON.parse(currentResultStr)
    
        console.log("data on second page:", currentResult)
        console.log("data on second page type:", typeof(currentResult))
    
    

    let alexlist = []

    alexlist = getAlex(currentResult.text)
    currentResult.agebias = currentResult.agebias.concat(alexlist) 
    
    console.log('newbias', currentResult.agebias)
}
   
    return(
        <React.Fragment>

        {currentResult &&

            <React.Fragment>
        <div className="App-left">
            <MyHighlight 
                        text={currentResult.text}
                        highlightlist={currentResult.agebias}
                />
            <MyToolTip currentResult = {currentResult}/>
        </div>
        <div className="App-right">
            
            <button className="result-button a-btn a-btn--block a-btn--grey" onClick={() => {setCurrentResult(null)}}>Scan Again</button> 
            <MySummary currentResult = {currentResult}/>
            
        </div>
        </React.Fragment>}
        </React.Fragment>  
    )
}