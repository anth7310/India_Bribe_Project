
# read data
my_data <- read.delim("../data.txt")


days <- weekdays(as.Date(my_data$date,'%Y-%m-%d'))
months <- months(as.Date(my_data$date,'%Y-%m-%d'))


states <- c(
    "AndhraPradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "DamanandDiu",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "HimachalPradesh",
    "JammuandKashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "MadhyaPradesh",
    "Maharashtra",
    "Orissa",
    "Punjab",
    "Rajasthan",
    "TamilNadu",
    "Telangana",
    "Tripura",
    "UttarPradesh",
    "Uttarakhand",
    "WestBengal"
)

# bar graphs - days and months
#------------------
# plot days
plot(table(days)[c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")],
     )

# plot months
plot(table(months)[c("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")])

#plot states
plot(table(my_data$state)[states], type="h", main="state freq.", 
     xlab="states", ylab="freq")




