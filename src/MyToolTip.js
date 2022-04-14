import React from 'react';
import ReactTooltip from 'react-tooltip'

export default function MyToolTip({currentResult}){

    var mylist = []
  
            Object.entries(currentResult.agebias).forEach( d => {

              mylist.push(
              <div key={d[1].id}>
              <ReactTooltip id={d[1].id} effect='solid'>
                    This word/phrase might cause:<br></br>
                    <strong>{d[1].category}</strong><br></br>
                    Reason:<br></br>
                    <strong>{d[1].reason}</strong>
              </ReactTooltip>
              </div>
              )
          })
          
 
  return mylist
}