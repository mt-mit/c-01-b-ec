// CoPilotで自動生成したコード(コメントから生成)
// generateProductsを置換して確認するためのコード
// GET http://127.0.0.1:8000/ec/products からデータを取得

import axios from 'axios';
import { Product } from './mockProducts';

export const fetchProducts = async (): Promise<Product[]> => {
    const { data } = await axios.get('http://localhost:8000/ec/products');
    const products: Product[] = [];

    // dataの中身をproductにpush 
    data.forEach((product:any) => {
        products.push({
            id: product.product_id,
            name: product.product_name,
            price: product.price,
            image: `/images/products/dummy.jpg`,
            description: 'dummy',
            categoryId: 1,
            reviews: [],
        });        
    });
    return products;
}

