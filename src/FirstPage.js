import React, { useState } from 'react';
// import {CurrentData} from './App.js';
import SecondPage from './SecondPage.js';
import './App.css';

export default function FirstPage(){


    const input = React.useRef();



    const [currentResult, setCurrentResult] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
  
    // const currentData = {
    //     input: '',
    //     result: currentResult
    
    // }

    function fetchData(){

        if (input.current.value === ''){
            alert('please submit valid text!')
        }
        else{
        console.log('sent to backend:', input.current.value);

        setIsLoading(true);
        console.log("begin loading")

        fetch("/api/submit", {
            method: "POST",
            headers: {
              'Content-Type' : 'application/json',
              'Accept': 'application/json'
            },
            body: JSON.stringify(input.current.value) 
            }).then(res => res.json())
                .then(data => {

                    if (data.text !== ''){

                        setIsLoading(false);
                        console.log("stop loading")
                        console.log("result from backend:", data)
                        console.log("current result:", currentResult)
                        setCurrentResult(data)   

                    }
                       
            })

        }
                
            
    }


    const OnSubmit = (ev) => {
        ev.preventDefault();

        fetchData()
          
      };


return(

    <React.Fragment>

    {currentResult
        ? 
          <React.Fragment>

          <SecondPage currentResultStr = {currentResult} setCurrentResult = {setCurrentResult}/>

         

          </React.Fragment>  
        :
        isLoading
                ?
                    <React.Fragment>
                    
                    <div className="App-left">
                    <div className="loading-box"><h2>Scanning... Please wait</h2></div>

                    <form className="my-form loading" onSubmit={OnSubmit}>
                            <textarea className="my-form-input" type="text" ref={input} />
                            <input className="my-form-button a-btn a-btn--block a-btn--grey" type="submit" value="Scan" />
                    </form>
                    </div>
            
                    <div className="App-right intro">
                    The New School has developed a scanning tool that uses three open-source libraries to scan ordinary text documents generally, and job postings/descriptions in particular, for potential diversity, equity, and inclusion issues resulting from the use of inappropriate, offensive, gender-coded, or otherwise objectionable phrasing. 
                    </div>
                    </React.Fragment> 
            
                
                :
                    <React.Fragment>
                    <div className="App-left">
                    <form className="my-form" onSubmit={OnSubmit}>
                            <textarea className="my-form-input" type="text" ref={input} />
                            <input className="my-form-button a-btn a-btn--block a-btn--grey" type="submit" value="Scan" />
                    </form>
                    </div>
            
                    <div className="App-right intro">
                    The New School has developed a scanning tool that uses three open-source libraries to scan ordinary text documents generally, and job postings/descriptions in particular, for potential diversity, equity, and inclusion issues resulting from the use of inappropriate, offensive, gender-coded, or otherwise objectionable phrasing. 
                    </div>
                    </React.Fragment> 
            
            
     
    }
    </React.Fragment>
)

}