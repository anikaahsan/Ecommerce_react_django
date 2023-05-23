import React,{useState,useEffect} from 'react';
import { Link } from 'react-router-dom';
import {Row,Col,Image,ListGroup,Button,Card} from 'react-bootstrap';
import Rating from '../components/Rating';


import axios from 'axios'
import {useParams } from 'react-router-dom'



function ProductScreen(){

    const params=useParams(); //returns a dict
    console.log(params)
    const {id }=useParams();

    const [product,setProduct]=useState([])

    useEffect(()=>{
        async function fetchproduct(){
           const {data}= await axios.get(`/api/products/${id}`)
           setProduct(data)
        }
       fetchproduct()
    },[])

    

    // const product=products.find((p)=>p._id == id)
    return(
        <div>
          
           <Link to='/' className='btn btn-light my-3'>Go Back</Link>
           <Row>
                <Col md={6} sm={12} >
                    <Image src={product.image} alt={product.name}/>
                </Col>
                <Col md={3} sm={12} >
                  <ListGroup variant='flush'>
                        <ListGroup.Item>
                        <h3>{product.name}</h3>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'}/>
                        </ListGroup.Item>

                        <ListGroup.Item>
                            Price:${product.price}
                        </ListGroup.Item>

                        <ListGroup.Item>
                           {product.description}
                        </ListGroup.Item>
                   
                  </ListGroup>
                </Col>
                <Col md={3} sm={12}>
                    <Card>
                        <ListGroup variant='flush'>
                            <ListGroup.Item>
                                <Row>
                                    <Col>
                                    Price:
                                    </Col>
                                    <Col>
                                    <strong>${product.price}</strong>
                                    </Col>
                                </Row>
                            </ListGroup.Item>

                            <ListGroup.Item>
                                <Row>
                                    <Col>
                                    Status
                                    </Col>
                                    <Col>
                                    {
                                      product.countInStock>0 ?
                                      'In Stock'  
                                      :'Stock Out'
                                    }
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Row>
                                    <Button className='btn-block' type='button' disabled={ product.countInStock==0 }>Add to Cart</Button>
                                </Row>
                            </ListGroup.Item>
                        </ListGroup>
                    </Card>
                </Col>
           </Row>
           
        </div>
    )

}
export default ProductScreen;