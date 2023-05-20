import React from 'react';


function Rating({ value ,text,color }){
    return(
        <div className='rating'>
            <span>
                <i style={{ color }} 
                   className={
                            // -----if-----
                               value >=1 ? 
                               'fas fa-star'
                            // -----else if-----------
                               :value >=0.5 ? 
                               'fas fa-star-half-alt'
                            // ---else ----------------
                               :'far fa-star'

                             }
                >

                </i>
            </span>
            <span>
                <i style={{ color }} 
                   className={
                            // -----if-----
                               value >=2 ? 
                               'fas fa-star'
                            // -----else if-----------
                               :value >=1.5 ? 
                               'fas fa-star-half-alt'
                            // ---else ----------------
                               :'far fa-star'

                             }
                >
                </i>
            </span>
            <span>
                <i style={{color } } 
                className={ 
                    value>=3 ?
                    'fas fa-star'
                    :value>=2.5?
                    'fas fa-star-half-alt'
                    :'far fa-star'
                }
                >

                </i>
            </span>
            <span>
                <i style={{color } } 
                   className={
                            // -----if-----
                               value >=4 ? 
                               'fas fa-star'
                            // -----else if-----------
                               :value >=3.5 ? 
                               'fas fa-star-half-alt'
                            // ---else ----------------
                               :'far fa-star'

                             }
                >
                </i>
            </span>
            <span>
                <i style={{ color }} 
                   className={
                            // -----if-----
                               value >=5 ? 
                               'fas fa-star'
                            // -----else if-----------
                               :value >=4.5 ? 
                               'fas fa-star-half-alt'
                            // ---else ----------------
                               :'far fa-star'

                             }
                >
                </i>
            </span>
            <span>
                {
                    text &&
                    text
                }
            </span>

        </div>
    )

}
export default Rating;