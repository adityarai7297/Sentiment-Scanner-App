import React, {useState} from 'react';
import FirstPage from './FirstPage';
import './App.css';

export const CurrentData = React.createContext();

export default function App() {

  
  // useEffect(() => {
  //   fetch('/api').then(res => res.json()).then(data => {
  //     setCurrentResult(data);
  //     console.log('get new result')
  //   });
  // }, [content]);

  // const [headerHandler, setHeaderHandler] = useState(null);
  // fetch('https://www.newschool.edu/Components/Handlers/HeaderHandler.ashx')
  //   .then(res => res.text())
  //   .then(res => {
  //       setHeaderHandler(res)
  //   })

    //     setCurrentResult(data);
    //     console.log('get new result')

  return (
    <React.Fragment>
    
    <div className="App">
      <div className="App-header m-pageHeader m-pageHeader--separator-all">
      
      <div className="m-pageHeader__heading">
       <div className="row">
         <div className="columns medium-13">
            <h1 className="m-pageHeader__title m-pageHeader__title--small"> DEI-SJ SCANNER</h1>
          </div>
        </div>
      </div>
        </div>
      <div className="App-body"> 
        <FirstPage />
      </div>
      
    </div>
    </React.Fragment>
  );
}

