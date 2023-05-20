import Footer from './components/Footer';
import Header from './components/Header';
import HomeScreen from './screens/HomeScreen';
import ProductScreen from './screens/ProductScreen';

import {Container } from 'react-bootstrap';
import { BrowserRouter  ,Route ,Routes} from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

function App() {
 
  return (
      <>
              <Header/>
            
              <main className='py-3'>
                <Container>
 
                          <Routes>
                                {/* <HomeScreen/> */}
                                <Route path='/'  element={ <HomeScreen/>} exact/>
                                <Route path='/product/:id' element={<ProductScreen/>}  />  {/* :id---->dynamic id */}
                                
                           </Routes>
    
                </Container>
              </main>
             
              <Footer/>
              </>
      
  );
}

export default App;
