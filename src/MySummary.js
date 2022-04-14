import React from 'react';

export default function MySummary({currentResult}){
var c1 = 0;
var c2 = currentResult.agebias.length

    for (let i = 0; i<currentResult.agebias.length; i++ ){
        if (currentResult.agebias[i].id === 'blank' ){
            c1 = 0 //no age bias, all counts go to alex's
            c2 = currentResult.agebias.length-1
            break
        }
        else if (currentResult.agebias[i].category === 'Age Bias'){
            c1 += 1
            c2 -= 1
        }
    }

    return (
    <div className="result-summary">
        <section className="m-sidebarModule">
        <h2 className="m-sidebarModule__title">Summary</h2>
        <ul><strong>The text being scanned has:</strong>
        <li>{c1} issues with age bias</li>
        <li>{c2} issues with insensitive, inconsiderate writing</li>
        </ul>
        </section>
    </div>
    )
}