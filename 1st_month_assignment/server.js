// const demandRoutes = require("./routes/demandRoutes")

// app.use("/api/demand", demandRoutes)
// const express = require("express")
// const mongoose = require("mongoose")
// const cors = require("cors")
// const bodyParser = require("body-parser")

// const farmerRoutes = require("./routes/farmerRoutes")
// const cropRoutes = require("./routes/cropRoutes")
// const priceRoutes = require("./routes/priceRoutes")

// const app = express()

// app.use(cors())
// app.use(bodyParser.json())

// mongoose.connect("mongodb://127.0.0.1:27017/farmerDB")
// .then(()=>console.log("MongoDB Connected"))
// .catch(err=>console.log(err))

// app.use("/api/farmers", farmerRoutes)
// app.use("/api/crops", cropRoutes)
// app.use("/api/price", priceRoutes)

// app.listen(5000, ()=>{
//     console.log("Server running on port 5000")
// })
const express = require("express")
const cors = require("cors")
const bodyParser = require("body-parser")

const connectDB = require("./config/db")

const farmerRoutes = require("./routes/farmerRoutes")
const cropRoutes = require("./routes/cropRoutes")
const priceRoutes = require("./routes/priceRoutes")
const demandRoutes = require("./routes/demandRoutes")

const app = express()

app.use(cors())
app.use(bodyParser.json())

// connect database
connectDB()

app.use("/api/farmers", farmerRoutes)
app.use("/api/crops", cropRoutes)
app.use("/api/price", priceRoutes)
app.use("/api/demand", demandRoutes)

app.listen(5000, () => {
    console.log("Server running on port 5000")
})